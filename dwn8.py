import pygal
wm=pygal.maps.world.World()
wm.title='North,South,South America'
wm.add('North America',['ca','mx','us'])
wm.add('Asia',['bd','in','pk'])
wm.render_to_file('Americas3.svg')
