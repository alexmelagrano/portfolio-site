# Helper function to return a dict of projects for the template

projects = [
        {
            'title': 'Portfolio Site v1',
            'body': 'First generation of this site.  Taught myself HTML/CSS and built this as an introduction to web '
                    'design across five weeks during the winter of 2016.  Learned HTML nesting, CSS, and how to steal \
                    jQuery code off the internet.',
            'tags': [
                {'name': 'HTML'},
                {'name': 'CSS'},
                {'name': 'jQuery'}
                     ],
            'link': {'text': 'Website',
                     'url': '/old-site/'}
        },
        {
            'title': 'isnortheasternopen',
            'body': 'Developed on a whim one Wednesday night in February 2017 after a friend suggested the idea, this '
                    'whimsical website is meant for Northeastern students to visit if they want to know if classes are'
                    'canceled.  This gave me a chance to learn more about AWS\'s static site hosting capabilities.',
            'tags': [
                {'name': 'AWS S3'},
                {'name': 'AWS Route53'},
                {'name': 'HTML'}
                     ],
            'link': {'text': 'isnortheasternopen.com',
                     'url': 'http://isnortheasternopen.com/'}
        },
        {
            'title': 'Stat Hacks',
            'body': 'Using a large database of college crime statistics, this web app allows you to graphically compare'
                    ' universities based on reported criminal incidents.  Fueled by Red Bull and snacks, Stat Hacks was'
                    ' designed and built during Northeastern\'s HuskyHacks2016 for The Huntington News, and served as a'
                    ' flash-introduction to large-scale data manipulation and representation.',
            'tags': [
                {'name': 'AngularJS'},
                {'name': 'Data Science'},
                {'name': 'Scss'}
                     ],
            'link': {'text': 'justagraph.co',
                     'url': 'http://www.justagraph.co/'}
        },
        {
            'title': 'DarkSky Weather App',
            'body': 'A simple weather app built on DarkSky\'s weather data API.  Developed largely during downtime at '
                    'my first co-op, this served as an introduction to AngularJS 1.x, and the Bourbon+Neat Sass '
                    'library.',
            'tags': [
                {'name': 'AngularJS'},
                {'name': 'DarkSky API'},
                {'name': 'Sass'}
                     ],
            'link': {'text': 'Github repo',
                     'url': 'https://github.com/alexmelagrano/DarkSky'}
        },
        {
            'title': 'Slack File Deletion',
            'body': 'A simple script used to clean up old uploaded files.  Developed during downtime at my first '
                    'co-op, I learned more about Python and AWS Lambda to prep for an upcoming project I was pulled '
                    'onto.',
            'tags': [
                {'name': 'Python'},
                {'name': 'AWS Lambda'},
                {'name': 'Slack API'}
                     ],
            'link': {'text': 'Github repo',
                     'url': 'https://github.com/alexmelagrano/Slack_File_Deletion'}
        }
    ]


# Simply returns the 'projects' array
def getProjects():
    return projects
