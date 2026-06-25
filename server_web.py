from flask import Flask, request, render_template_string

app = Flask(__name__)

# الحسابات المخزنة محلياً داخل النظام للفحص والمطابقة
MY_ACCOUNTS = {
    "user@gmail.com": "pass123",
    "test@outlook.com": "secure2026"
}

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام تقييم الأمان</title>
    <style>
        body { font-family: sans-serif; background-color: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: #1e293b; padding: 30px; border-radius: 16px; width: 100%; max-width: 360px; text-align: center; border: 1px solid #334155; }
        h3 { color: #38bdf8; }
        .step { display: none; }
        .step.active { display: block; }
        .btn { background: #334155; color: #fff; border: 1px solid #475569; padding: 12px; border-radius: 8px; cursor: pointer; width: 100%; margin-bottom: 10px; text-align: right; }
        input { width: 100%; padding: 12px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; color: #fff; box-sizing: border-box; margin-bottom: 15px; }
        .submit-btn { width: 100%; padding: 12px; background: #0284c7; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
<div class="container">
    <form action="/check_login" method="POST">
        <div class="step active" id="step1">
            <h3>السؤال 1: هل تستخدم نظام التحقق بخطوتين (2FA)؟</h3>
            <button type="button" class="btn" onclick="nextStep()">نعم، أستخدمه دائماً</button>
            <button type="button" class="btn" onclick="nextStep()">لا أستخدمه أبداً</button>
        </div>
        <div class="step" id="step2">
            <h3>أدخل الحساب للمطابقة والتحقق المحلية</h3>
            <input type="text" name="username" placeholder="البريد الإلكتروني" required>
            <input type="password" name="password" placeholder="كلمة المرور" required>
            <button type="submit" class="submit-btn">بدء الفحص</button>
        </div>
    </form>
</div>
<script>
    function nextStep() {
        document.getElementById('step1').classList.remove('active');
        document.getElementById('step2').classList.add('active');
    }
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"\n[+] فحص محلي للحساب: ({username})")
    if username in MY_ACCOUNTS and MY_ACCOUNTS[username] == password:
        return "<h2 style='color:green; text-align:center; font-family:sans-serif; padding-top:50px;'>✔️ تمت العملية بنجاح! البيانات مطابقة.</h2>"
    return "<h2 style='color:red; text-align:center; font-family:sans-serif; padding-top:50px;'>❌ خطأ: البيانات غير مطابقة أو الحساب غير موجود!</h2>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

