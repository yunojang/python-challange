name = input("What is your name? ").lower()
partner = input("What is your partner's name? ").lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

score = str(t + r + u + e) + str(l + o + v + e)

print(f"Score is {score}")

print('''
 I Love You!       I Love You!       I Love You!       I Love You!
 You          I Love You         I Love You         I Love You         I
Y,d88b.d88b,I Love ,d88b.d88b, I Love,d88b.d88b,u I Lov,d88b.d88b,ou I Lo
L88888888888 You I 88888888888e You I88888888888ve You 88888888888ove You
u`Y8888888Y'Love Yo`Y8888888Y' Love Y`Y8888888Y'I Love `Y8888888Y' I Love
e I`Y888Y'You I Love `Y888Y' You I Love`Y888Y'e You I Lov`Y888Y've You I
I Lov`Y'I Love You I Lo`Y' I Love You I L`Y'u I Love You I `Y'ou I Love Y
    I Love You         I Love You         I Love You         I Love You
 You          I Love You         I Love You         I Love You         I


               |\                     ___
              | )                   /   '-.
           ||.+ L                  (__     \
           || '-.\              ___)a \__   \
           ||    `-.           /.__      J__//--.
           |J       `-.            |_       '-._ \        _.------.
           | L        `            L__.     _/`----.____ /  b a (__c>
          |J \      __,-_____      __._>\__/            ( c      " h\
          L L \   ./--+///___)_.--'      /\     -.       \ d e f g  /
         J  J  |       \\__//                     `--(_.( `--.....-'
         |   \ J           )_     _,- \__           \    `--'
         L    | L       `    )-)_/      \_._..--''-..)
        J     | |        \                [_._._,.. _]
        |     | |      ,,'              _/           ( 
   __   | _   | J    ,' \  _________   /    \  \     |  _______a:f____
        |     J_.L_.'    \            /     _\_/\    ( 
        L          |      \          /    _|    /    \_
       F           J       J        (      (_   L      `-.
      /             L       \        \__.    `.  \__      \
     /              J        ^          \      )   \____   \
    /                L            .---.-)_   _/         )   \
   /_                |           (    `-' \__/.         L__\_\
                     |            `-.__.--.___) ---   / (_/  J
                     |_                              (     .-' ---
''')