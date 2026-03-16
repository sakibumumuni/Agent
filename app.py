from flask import Flask, request, render_template
import os
import asyncio
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
)



async def main(userQuery: str):
    chunks = []
    async for message in query(
        prompt=userQuery,
        options=ClaudeAgentOptions(
            allowed_tools=[
                "Read",
                "Write",
                "Edit",
                "Bash",
                "Glob",
                "Grep",
                "WebSearch",
            ],
            permission_mode="acceptEdits",
        ),
    ):
        
        # Return human-readable output
           if isinstance(message, AssistantMessage):
             for block in message.content:
                if isinstance(block, TextBlock):
                    chunks.append(block.text)
    return "".join(chunks)

app = Flask(__name__)




@app.route('/chat', methods=['POST', 'GET'])
def chat_with ():
          if request.method == 'POST':
            chat = request.form.get('chat')
            print(f'Received {chat}')
            response = asyncio.run(main(chat))
            print(f'Response {response}')
            return render_template('agentui.html', chat = chat, response = response)
          return render_template('agentui.html')
    



if __name__  ==  '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)





    
