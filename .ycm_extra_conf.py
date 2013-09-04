flags = [
	'-Wall',
	'-Wextra',
	'-Werror',
	'-std=c++11',
	'-xc++',
	'-I.',
	'-Iinclude',
	'-Isrc'
]

def FlagsForFile(filename):
	return {
		'flags': flags,
		'do_cache': True
	}
