"""Expected results for some tests"""

from mock import call
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')

karaoke_xml = """<smil>
  <head>
    <layout> <!--Create the canvas and two display regions -->
    	<root-layout width="248" height="300"
		background-color="blue" />
	     <region id="a" top="20" left="64" />
	     <region id="b" top="120" left="20"/>
	     <region id="text_area" top="100" left="20"/>
     </layout>
  </head>
  <body>
     <par>
	<img src="http://www.content-networking.com/smil/hello.jpg"
	     region="a"
	     begin="2s"
	     dur="36s"/> <!--Display "Hello" image now for 6 seconds -->
	<img src="http://www.content-networking.com/smil/earthrise.jpg"
	     region="b"
	     begin="12s"
	     end="48s"/> <!--Display the "World" image after 12 seconds -->
	<audio src="http://www.content-networking.com/smil/hello.wav"
	     begin="1s"/> <!-- Begin the audio after 1 seconds -->
	<textstream src="http://gsyc.es/~grex/letra.rt" region="text_area" fill="freeze" />
            <audio src="cancion.ogg" begin="4s"/>
    </par>
  </body>
</smil>
"""

karaoke_tags = [
    {'attrs': [('width', '248'), ('height', '300'), ('background-color', 'blue')],
     'name': 'root-layout'},
    {'attrs': [('id', 'a'), ('top', '20'), ('left', '64')],
     'name': 'region'},
    {'attrs': [('id', 'b'), ('top', '120'), ('left', '20')],
     'name': 'region'},
    {'attrs': [('id', 'text_area'), ('top', '100'), ('left', '20')],
     'name': 'region'},
    {'attrs': [('src', 'http://www.content-networking.com/smil/hello.jpg'),
               ('region', 'a'), ('begin', '2s'), ('dur', '36s')],
     'name': 'img'},
    {'attrs': [('src', 'http://www.content-networking.com/smil/earthrise.jpg'),
               ('region', 'b'), ('begin', '12s'), ('end', '48s')],
     'name': 'img'},
    {'attrs': [('src', 'http://www.content-networking.com/smil/hello.wav'),
               ('begin', '1s')],
     'name': 'audio'},
    {'attrs': [('src', 'http://gsyc.es/~grex/letra.rt'),
               ('region', 'text_area'), ('fill', 'freeze')],
     'name': 'textstream'},
    {'attrs': [('src', 'cancion.ogg'), ('begin', '4s')],
     'name': 'audio'}
]

karaoke_str = """root-layout\twidth="248"\theight="300"\tbackground-color="blue"
region\tid="a"\ttop="20"\tleft="64"
region\tid="b"\ttop="120"\tleft="20"
region\tid="text_area"\ttop="100"\tleft="20"
img\tsrc="http://www.content-networking.com/smil/hello.jpg"\tregion="a"\tbegin="2s"\tdur="36s"
img\tsrc="http://www.content-networking.com/smil/earthrise.jpg"\tregion="b"\tbegin="12s"\tend="48s"
audio\tsrc="http://www.content-networking.com/smil/hello.wav"\tbegin="1s"
textstream\tsrc="http://gsyc.es/~grex/letra.rt"\tregion="text_area"\tfill="freeze"
audio\tsrc="cancion.ogg"\tbegin="4s"
"""

karaoke_json = [
    {'attrs': {'background-color': 'blue', 'height': '300', 'width': '248'},
     'name': 'root-layout'},
    {'attrs': {'id': 'a', 'left': '64', 'top': '20'},
     'name': 'region'},
    {'attrs': {'id': 'b', 'left': '20', 'top': '120'},
     'name': 'region'},
    {'attrs': {'id': 'text_area', 'left': '20', 'top': '100'},
     'name': 'region'},
    {'attrs': {'begin': '2s', 'dur': '36s', 'region': 'a',
               'src': 'http://www.content-networking.com/smil/hello.jpg'},
     'name': 'img'},
    {'attrs': {'begin': '12s', 'end': '48s', 'region': 'b',
               'src': 'http://www.content-networking.com/smil/earthrise.jpg'},
     'name': 'img'},
    {'attrs': {'begin': '1s',
               'src': 'http://www.content-networking.com/smil/hello.wav'},
     'name': 'audio'},
    {'attrs': {'fill': 'freeze', 'region': 'text_area',
               'src': 'http://gsyc.es/~grex/letra.rt'},
     'name': 'textstream'},
    {'attrs': {'begin': '4s', 'src': 'cancion.ogg'},
     'name': 'audio'}]

smil_xml = """<smil>
  <head>
    <layout>
      <root-layout width="500" height="400" />
	  <region id="arriba" top="0" left="0" />
	  <region id="abajo" top="120" left="0"/>
    </layout>
  </head>
  <body>
    <par>
      <img src="http://www.content-networking.com/smil/earthrise.jpg"
               region="abajo"
               begin="48s"/>
      <img src="http://www.content-networking.com/smil/hello.jpg"
               region="arriba" />
    </par>
  </body>
</smil>
"""

smil_tags = [
    {'attrs': [('width', '500'), ('height', '400')],
     'name': 'root-layout'},
    {'attrs': [('id', 'arriba'), ('top', '0'), ('left', '0')],
     'name': 'region'},
    {'attrs': [('id', 'abajo'), ('top', '120'), ('left', '0')],
     'name': 'region'},
    {'attrs': [('src', 'http://www.content-networking.com/smil/earthrise.jpg'),
               ('region', 'abajo'), ('begin', '48s')],
     'name': 'img'},
    {'attrs': [('src', 'http://www.content-networking.com/smil/hello.jpg'),
               ('region', 'arriba')],
     'name': 'img'}]

smil_str = """root-layout\twidth="500"\theight="400"
region\tid="arriba"\ttop="0"\tleft="0"
region\tid="abajo"\ttop="120"\tleft="0"
img\tsrc="http://www.content-networking.com/smil/earthrise.jpg"\tregion="abajo"\tbegin="48s"
img\tsrc="http://www.content-networking.com/smil/hello.jpg"\tregion="arriba"
"""

smil_json = [
    {'attrs': {'height': '400', 'width': '500'},
     'name': 'root-layout'},
    {'attrs': {'id': 'arriba', 'left': '0', 'top': '0'},
     'name': 'region'},
    {'attrs': {'id': 'abajo', 'left': '0', 'top': '120'},
     'name': 'region'},
    {'attrs': {'begin': '48s', 'region': 'abajo',
               'src': 'http://www.content-networking.com/smil/earthrise.jpg'},
     'name': 'img'},
    {'attrs': {'region': 'arriba',
               'src': 'http://www.content-networking.com/smil/hello.jpg'},
     'name': 'img'}]

calls_urlretrieve = [
    call('http://www.content-networking.com/smil/hello.jpg', 'fichero-0.jpg'),
    call('http://www.content-networking.com/smil/earthrise.jpg', 'fichero-1.jpg'),
    call('http://www.content-networking.com/smil/hello.wav', 'fichero-2.wav'),
    call('http://gsyc.es/~grex/letra.rt', 'fichero-3.rt')
]
