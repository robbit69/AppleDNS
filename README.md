# AppleDNS

苹果的移动设备，例如 iPhone 和 iPad 设备。只能设置 WiFi 下的 DNS，无法设置蜂窝数据下的 DNS，所以这里是一个描述文件，直接指定了 114.114.114.114 的 DNS。

## 如何使用

使用你的苹果设备点击下面的链接或 AppleDNS-DoT.mobileconfig 文件的 raw 按钮，即可自动下载描述文件，然后在设置中信任即可。

114 的 DNS 可以解决很多解析错误的问题，如果需要其他地址的 DNS 可以 fork 一下然后修改对应字段即可，安装方式同上。

另一个更好的方法是直接使用 Surge 来按需指定 DNS，更方便更灵活，有需要可以自行谷歌。

该描述文件启用了基于 TLS 的加密 DNS（DoT），服务器名称设定为 dot.114dns.com，对应的服务器地址为 114.114.114.114，与上文描述保持一致。

https://raw.githubusercontent.com/robbit69/AppleDNS/refs/heads/master/AppleDNS-DoT.mobileconfig
