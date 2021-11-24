from quart import Quart, request, send_file

app = Quart(__name__)

@app.route("/")
async def main():
    return "<center><b>POC for actual Discord image exploitation.</b><br>Send <a href='/kinky.gif'>this link</a> on Discord, and while using the electron client, compare the results of the discord image preview vs opening the original.</center>"

@app.route('/kinky.gif')
async def POC():
    userAgent = request.headers.get('User-Agent')
    print('[log]: useragent ' + userAgent + ' requested gif.')
    if not 'Electron/' in userAgent and not 'discord/' in userAgent:
        return "<p>There could've been a payload here, where I sent your data off to some random server.</p>"
    else:
        return await send_file('actualGif.gif')

@app.route('/always.gif')
async def retGif():
    return await send_file('actualGif.gif')
