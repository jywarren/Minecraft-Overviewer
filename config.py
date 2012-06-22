# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['p.irateship'] = "../world-2012-06-09/"

# Define where to put the output here.
outputdir = "../new-world/"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

def signFilter(poi):
    if poi['id'] == 'Sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

renders["render1"] = {
        'world': 'p.irateship',
        'title': 'Day',
        'markers': [dict(name="All signs", filterFunction=signFilter)],
	'defaultZoom': -2
}

# This example is the same as above, but rotated
#renders["render2"] = {
#        'world': 'My World',
#        'northdirection': 'upper-right',
#        'title': 'Upper-right north direction',
#}

# Here's how to do a nighttime render. Also try "smooth_night" instead of "night"
renders["render3"] = {
        'world': 'p.irateship',
        'title': 'Night',
        # Notice how this overrides the rendermode default specified above
        'rendermode': 'night'
}

