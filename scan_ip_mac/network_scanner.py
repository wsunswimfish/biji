from netmiko import ConnectHandler
import time
import ipaddress
import pandas as pd
from datetime import datetime
import re

class NetworkScanner:
    def __init__(self, switch_ip, username, password):
        self.device_info = {
            'device_type': 'huawei',  # 华为设备类型
            'host': switch_ip,
            'username': username,
            'password': password,
            'global_delay_factor': 2,  # 增加延迟因子，提高可靠性
            'port':10022,
        }
        self.connection = None
        self.arp_cache = {}
        
    def connect_switch(self):
        """连接到核心交换机"""
        try:
            print("正在连接交换机...")
            self.connection = ConnectHandler(**self.device_info)
            print("连接成功！")
            return True
        except Exception as e:
            print(f"连接交换机失败: {str(e)}")
            return False

    def check_connection(self):
        """检查连接状态，如果断开则重连"""
        try:
            # 尝试发送简单命令测试连接
            self.connection.send_command('display clock')
            return True
        except Exception:
            print("连接已断开，尝试重新连接...")
            try:
                self.connection.disconnect()
            except:
                pass
            return self.connect_switch()

    def execute_command(self, command, expect_string=None):
        """执行命令并处理连接状态"""
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                if not self.check_connection():
                    raise Exception("无法重新建立连接")
                
                if expect_string:
                    output = self.connection.send_command(command, expect_string=expect_string)
                else:
                    output = self.connection.send_command(command)
                return output
                
            except Exception as e:
                retry_count += 1
                print(f"执行命令失败 (尝试 {retry_count}/{max_retries}): {str(e)}")
                time.sleep(2)
                
        raise Exception("执行命令失败，已超过最大重试次数")

    def get_arp_table(self):
        """获取交换机的ARP表"""
        try:
            arp_output = self.execute_command('display arp')
            return self._parse_arp_output(arp_output)
        except Exception as e:
            print(f"获取ARP表失败: {str(e)}")
            return []

    def _parse_arp_output(self, arp_output):
        """解析ARP表输出"""
        # 定义匹配模式
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # IP地址格式
        mac_pattern = r'([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4}'  # MAC地址格式 (XXXX-XXXX-XXXX)
        interface_pattern = r'(GE|XGE|ME|Eth|Vlanif)\S+'  # 接口格式
        
        arp_entries = []
        for line in arp_output.split('\n'):
            # 查找该行中的IP、MAC和接口
            ip_match = re.search(ip_pattern, line)
            mac_match = re.search(mac_pattern, line)
            interface_match = re.search(interface_pattern, line)
            
            # 只有当三者都匹配时才认为是有效的ARP条目
            if ip_match and mac_match and interface_match:
                entry = {
                    'ip': ip_match.group(),
                    'mac': mac_match.group(),
                    'interface': interface_match.group(),
                    'type': 'dynamic'  # 默认类型
                }
                
                # 尝试判断类型（静态/动态）
                if 'static' in line.lower():
                    entry['type'] = 'static'
                
                arp_entries.append(entry)
                self.arp_cache[entry['ip']] = entry
                
        return arp_entries

    def scan_network(self, network):
        """扫描指定网段并收集设备信息"""
        devices = []
        net = ipaddress.ip_network(network)
        batch_size = 5  # 减小批量大小，避免设备负载过高
        ip_batch = []
        
        print(f"开始扫描网段 {network}...")
        
        # 批量执行ping
        for ip in net.hosts():
            ip_str = str(ip)
            ip_batch.append(ip_str)
            
            if len(ip_batch) >= batch_size:
                self._process_ip_batch(ip_batch)
                ip_batch = []
        
        # 处理剩余的IP
        if ip_batch:
            self._process_ip_batch(ip_batch)
        
        # 获取最终的ARP表
        arp_entries = self.get_arp_table()
        
        # 整理设备信息
        for entry in arp_entries:
            if ipaddress.ip_address(entry['ip']) in net:
                devices.append(entry)
        
        return devices

    def _process_ip_batch(self, ip_batch):
        """批量处理IP地址"""
        for ip in ip_batch:
            try:
                # 使用华为设备的ping命令
                command = f'ping -c 1 {ip}'
                self.execute_command(command, expect_string=r'>')
            except Exception as e:
                print(f"ping {ip} 时发生错误: {str(e)}")
        
        # 等待ARP表更新
        time.sleep(2)

    def scan_networks(self, networks):
        """扫描多个网段"""
        all_devices = []
        total_networks = len(networks)
        
        for i, network in enumerate(networks, 1):
            print(f"正在扫描第 {i}/{total_networks} 个网段: {network}")
            devices = self.scan_network(network)
            all_devices.extend(devices)
            print(f"网段 {network} 扫描完成，发现 {len(devices)} 个设备")
        
        return all_devices

    def export_results(self, devices, filename=None):
        """导出扫描结果到CSV文件"""
        if not filename:
            filename = f"network_scan_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        
        df = pd.DataFrame(devices)
        # 重新排列列顺序
        columns = ['ip', 'mac', 'interface', 'type']
        df = df.reindex(columns=columns)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"扫描结果已保存到 {filename}")
        print(f"共发现 {len(devices)} 个设备")

def main():
    # 配置参数
    switch_ip = "172.20.10.10"
    username = "wfdladmin"
    password = "2186&xxzxvty"
    networks = ["10.141.192.0/24","10.141.193.0/24"]

    # 创建扫描器实例
    scanner = NetworkScanner(switch_ip, username, password)
    
    try:
        # 连接交换机
        if not scanner.connect_switch():
            return
        
        # 扫描网络并收集设备信息
        print("开始网络扫描...")
        devices = scanner.scan_networks(networks)
        
        # 导出结果
        scanner.export_results(devices)
        
    except Exception as e:
        print(f"程序执行过程中发生错误: {str(e)}")
    finally:
        if scanner.connection:
            scanner.connection.disconnect()
            print("已断开与交换机的连接")

if __name__ == "__main__":
    main() 