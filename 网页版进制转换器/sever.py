import http.server
import socketserver
import webbrowser
import os

# 修改文件名去除空格
original_filename = "新建 文本文档.html"
new_filename = "converter.html"

# 重命名文件（仅需运行一次）
if os.path.exists(original_filename) and not os.path.exists(new_filename):
    os.rename(original_filename, new_filename)

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# 自动打开浏览器
webbrowser.open_new_tab(f"http://localhost:{PORT}/{new_filename}")

# 启动服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器已启动，访问地址：http://localhost:{PORT}/{new_filename}")
    print("按Ctrl+C停止服务器")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")