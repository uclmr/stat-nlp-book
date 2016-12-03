from IPython.core.display import HTML

import uuid


# https://www.embeddedrelated.com/showarticle/599.php

def edit_svg(filename, height="400"):
    svg_id = str(uuid.uuid1())

    # load the file
    # populate svg element on page
    # javascript code that edits svg
    # trigger that stores current svg element in original file
    html = """
    <div id='""" + svg_id + """'>
    <!--    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
    </svg> -->
    <script>
        requirejs.config({
            paths: {
                'drupyter': ['/files/javascript/drupyter'],
                'snap.svg': ['/files/javascript/snap.svg']
                                                      // strip .js ^, require adds it back
            },
            urlArgs: "bust=" + (new Date()).getTime()
        });
        require(['snap.svg','drupyter'], function() {
            console.log("Drupyter Loaded");
            drupyter = new Drupyter('#""" + svg_id + """','""" + filename + """',{ width: '100%', height: '""" + height+ """'});
        });
    </script>
    """
    return HTML(html)
