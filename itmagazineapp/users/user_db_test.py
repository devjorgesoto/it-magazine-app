from .models import User


def prepopulate_db_user ():

    user_obj = User.objects.all()

    if not user_obj:

        marynova = User.objects.create( first_name = 'mary' , last_name = 'nova', username='marynova', email = 'marynova@example.com', password='marynova', short_description = default_short_description() , long_description = default_long_description() )
    
        annafrancis = User.objects.create( first_name = 'anna' , last_name = 'francis', username='annafrancis', email = 'annafrancis@example.com', password='annafrancis', short_description = default_short_description() , long_description = default_long_description() )

        taylormiller = User.objects.create( first_name = 'mia' , last_name = 'carter', username='taylormiller', email = 'miacarter@example.com', password='taylormiller', short_description = default_short_description() , long_description = default_long_description())

        wrightmurray = User.objects.create( first_name = 'wright' , last_name = 'murray', username='wrightmurray', email = 'wrightmurray@example.com', password='wrightmurray', short_description = default_short_description() , long_description = default_long_description() )

        wilsonstewart = User.objects.create( first_name = 'wilson' , last_name = 'stewart', username='wilsonstewart', email = 'wilsonstewart@example.com', password='wilsonstewart', short_description = default_short_description() , long_description = default_long_description() )

        madelynerin = User.objects.create( first_name = 'madelyn' , last_name = 'erin', username='madelynerin', email = 'madelynerin@example.com', password='madelynerin', short_description = default_short_description() , long_description = default_long_description() )
    
        alexanderaleman = User.objects.create( first_name = 'alexander' , last_name = 'aleman', username='alexanderaleman', email = 'alexanderaleman@example.com', password='alexanderaleman', short_description = default_short_description() , long_description = default_long_description() )

        toniamin = User.objects.create( first_name = 'toni' , last_name = 'amin', username='toniamin', email = 'toniamin@example.com', password='toniamin', short_description = default_short_description() , long_description = default_long_description() )

        gracearmani = User.objects.create( first_name = 'grace' , last_name = 'armani', username='gracearmani', email = 'gracearmani@example.com', password='gracearmani', short_description = default_short_description() , long_description = default_long_description() )

        arneyblake = User.objects.create( first_name = 'arney' , last_name = 'blake', username='arneyblake', email = 'arneyblake@example.com', password='arneyblake', short_description = default_short_description() , long_description = default_long_description() )

        print('***Pre-populating user list***')

    else :

        print('***User list pre-populated***')

def default_short_description():
    return 'Etiam vitae lacinia sapien. Duis semper nisi ac dui convallis auctor.'

def default_long_description():
    return 'Suspendisse tincidunt malesuada ipsum imperdiet dictum. Suspendisse nec consectetur nulla, et hendrerit ante. Integer sit amet urna mauris. Pellentesque eget pharetra odio, vitae tincidunt lectus. Maecenas nulla elit, congue a interdum sit amet, posuere eget tellus. Morbi congue dui sit amet est malesuada luctus. Etiam non neque id tellus tempor dictum at et nisl. In eu velit commodo, facilisis lacus ut, lacinia odio. Donec sed rutrum nulla. Phasellus sodales consequat diam, sit amet scelerisque dui feugiat ut. Vivamus nec fermentum quam. In nec rutrum neque, vel tincidunt lorem. Vestibulum consectetur nunc id interdum varius. In vulputate nunc mollis dui facilisis aliquam. Donec consectetur viverra ligula ut posuere. Vivamus ac lacus eget risus tincidunt rutrum sed a purus.'