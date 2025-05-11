import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "thirumalaivasangj@gmail.com"
receiver_email = "tg9424@srmist.edu.in"
app_password = "vbqd fksv fxcc lnfz"  # Your Gmail App Password

# Subject and HTML body
subject = "🎉 Congratulations – You've Been Shortlisted for the Hackathon!"

html_content = """
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <h2 style="color: #4CAF50;">🎉 Congratulations!</h2>
    <p>We are thrilled to inform you that you have been <strong>shortlisted</strong> for our upcoming <strong>Hackathon</strong>! 🖥️🚀</p>

    <h3 style="color: #333;">🧠 Hackathon Format</h3>
    <ol>
      <li><strong>Round 1 – Idea Presentation:</strong> Share your innovative concept and how it solves a real-world problem.</li>
      <li><strong>Round 2 – Final Round:</strong> Implement and showcase your working prototype to the judging panel.</li>
    </ol>

    <h3 style="color: #333;">📍 Event Instructions</h3>
    <ul>
      <li>✅ Please bring your <strong>laptop</strong>, <strong>charger</strong>, and any other essential equipment.</li>
      <li>✅ Carry your <strong>college ID card</strong> for verification at the venue.</li>
      <li>✅ Ensure you <strong>arrive on time</strong> to avoid disqualification.</li>
    </ul>

    <p>Kindly join the official WhatsApp group for real-time updates and communication:<br>
    👉 <a href="https://chat.whatsapp.fake/invite123">Join WhatsApp Group</a></p>

    <p>We can’t wait to see your creativity and problem-solving skills in action! 💡✨<br>
    Wishing you the very best!</p>

    <p style="margin-top: 20px;">Warm regards,<br>
    <strong>Hackathon Organizing Committee</strong></p>
  </body>
</html>
"""

# Compose and send email
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
message.attach(MIMEText(html_content, "html"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("✅ Email sent successfully.")
except Exception as e:
    print("❌ Failed to send email:", e)
