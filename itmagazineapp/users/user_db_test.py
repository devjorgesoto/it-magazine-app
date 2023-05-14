from .models import User


def prepopulate_db_user ():

    user_obj = User.objects.all()

    if not user_obj:

        marynova = User.objects.create( first_name = 'mary' , last_name = 'nova', username='marynova', email = 'marynova@example.com', password='marynova' )
    
        annafrancis = User.objects.create( first_name = 'anna' , last_name = 'francis', username='annafrancis', email = 'annafrancis@example.com', password='annafrancis' )

        taylormiller = User.objects.create( first_name = 'mia' , last_name = 'carter', username='taylormiller', email = 'miacarter@example.com', password='taylormiller' )

        wrightmurray = User.objects.create( first_name = 'wright' , last_name = 'murray', username='wrightmurray', email = 'wrightmurray@example.com', password='wrightmurray' )

        wilsonstewart = User.objects.create( first_name = 'wilson' , last_name = 'stewart', username='wilsonstewart', email = 'wilsonstewart@example.com', password='wilsonstewart' )

        madelynerin = User.objects.create( first_name = 'madelyn' , last_name = 'erin', username='madelynerin', email = 'madelynerin@example.com', password='madelynerin' )
    
        alexanderaleman = User.objects.create( first_name = 'alexander' , last_name = 'aleman', username='alexanderaleman', email = 'alexanderaleman@example.com', password='alexanderaleman' )

        toniamin = User.objects.create( first_name = 'toni' , last_name = 'amin', username='toniamin', email = 'toniamin@example.com', password='toniamin' )

        gracearmani = User.objects.create( first_name = 'grace' , last_name = 'armani', username='gracearmani', email = 'gracearmani@example.com', password='gracearmani' )

        arneyblake = User.objects.create( first_name = 'arney' , last_name = 'blake', username='arneyblake', email = 'arneyblake@example.com', password='arneyblake' )

        print('***Pre-populating user list***')

    else :

        print('***User list pre-populated***')

   