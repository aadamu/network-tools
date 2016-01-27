
def get_html_head():

    html_head = '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                    <title>Network Tools</title>

                    <!-- Bootstrap -->
                    <link href="static/css/bootstrap.min.css" rel="stylesheet">
                </head>
            '''
    return(html_head)


def get_bootstrap():

    bootstrap = '''
                <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
                <script src="/static/js/jquery-1.12.0.js"></script>
                <!-- Include all compiled plugins (below), or include individual files as needed -->
                <script src="static/js/bootstrap.min.js"></script>
                '''
    return(bootstrap)

def get_nav():

    web_nav = '''
                <nav class="navbar navbar-inverse navbar-fixed-top">
                  <div class="container">
                    <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">Network Tools</a>
                    </div>
                    <div id="navbar" class="collapse navbar-collapse">
                      <ul class="nav navbar-nav">
                        <li><a href="/">Home</a></li>
                        <li><a href="/cisco7">Decoder</a></li>
                        <li><a href="/ciscostatus">Device Status</a></li>
                      </ul>
                    </div><!--/.nav-collapse -->
                  </div>
                </nav>
                '''
    return (web_nav)

