import openai
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# GPT API key (replace with your actual API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        if self.path == '/summarize':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            email_content = json.loads(post_data).get('email', '')

            # GPT Summarization
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Summarize this email: {email_content}",
                    max_tokens=150
                )
                summary = response['choices'][0]['text'].strip()
                self._send_response({"summary": summary})
            except Exception as e:
                self._send_response({"error": str(e)}, 500)

        elif self.path == '/detect_action':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            email_content = json.loads(post_data).get('email', '')

            # Action detection using GPT
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Identify actions or tasks in this email: {email_content}",
                    max_tokens=150
                )
                actions = response['choices'][0]['text'].strip()
                self._send_response({"actions": actions})
            except Exception as e:
                self._send_response({"error": str(e)}, 500)

        elif self.path == '/generate_reply':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            email_content = json.loads(post_data).get('email', '')

            # GPT-based reply generation
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Write a professional reply for this email: {email_content}",
                    max_tokens=200
                )
                reply = response['choices'][0]['text'].strip()
                self._send_response({"reply": reply})
            except Exception as e:
                self._send_response({"error": str(e)}, 500)

        elif self.path == '/detect_spam':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            email_content = json.loads(post_data).get('email', '')

            # Dummy spam detection
            spam_keywords = ['win', 'free', 'lottery']
            is_spam = any(keyword in email_content.lower() for keyword in spam_keywords)
            self._send_response({"is_spam": is_spam})

        else:
            self._send_response({"error": "Invalid endpoint"}, 404)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
