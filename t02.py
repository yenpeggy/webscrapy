from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook 端點
@app.route('/webhook', methods=['POST'])
def webhook():
    # 獲取請求的 JSON 數據
    data = request.json

    # 打印接收到的數據（用於調試）
    print("Received data:", data)

    # 在這裡處理 Webhook 數據
    # 例如：根據數據執行某些操作，或存儲到數據庫

    # 返回成功的響應
    return jsonify({'status': 'success', 'message': 'Webhook received!'})

# 主程式入口
if __name__ == '__main__':
    # 運行伺服器，監聽 IP 34.80.121.209 和 Port 8080
    app.run(host='0.0.0.0', port=8080)