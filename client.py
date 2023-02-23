from vidstream import ScreenShareClient

sender = ScreenShareClient('192.168.100.155', 8080)

sender.start_stream()