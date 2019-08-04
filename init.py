from aiohttp import web
import subprocess

routes = web.RouteTableDef()
array = []

@routes.get('/')
@routes.get('/connections')
async def all(request):
    return web.json_response(array)


@routes.post('/connections')
async def add_connection(request):
    data = await request.post()
    print(data['connection'])
    array.append(data['connection'])
    return web.json_response(array)


@routes.get('/check/{host}')
async def check_connection(request):
    host = format(request.match_info['host'])
    output = ping(host, None)
    print(output)
    return web.json_response({"success": output})

@routes.get('/check/{host}/port/{port}')
async def check_connection_with_port(request):
    host = format(request.match_info['host'])
    port = format(request.match_info['port'])
    output = ping(host,port)
    print(output)
    return web.json_response({"success": output})

def ping(connection, port):
    try:
        if port:
            subprocess.check_output(["nc", "-vz", connection, port])
            return True
        else:
            subprocess.check_output(["ping", "-c", "1", connection])
            return True                      
    except subprocess.CalledProcessError:
        return False

app = web.Application()
app.add_routes(routes)
web.run_app(app)