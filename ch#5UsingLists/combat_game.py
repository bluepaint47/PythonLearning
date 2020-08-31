stock = {'shield':(15,20,50),
             'sword':(60,60,40),
             'dagger':(25,30,50),
             'helberd':(80,80,30),
             'club':(15,30,30),
             'flail':(50,70,45),
             'hammer':(99,100,20),
             'cuirass':(30,45,20),
             'armour':(101,100,0),
             'lantern':(10,5,30),
             'pole':(10,5,50),
             'rope':(10,5,70)}
armour_types = set(['shield','cuirass','armour'])         
hits = ('hits','bashes','smites','whacks',
              'shreds','mutilates','lacerates','annihilates')
misses = ('misses', 'nearly hits', 'fails to connact with',
             'swipes wildly at','flails inefectually at'
             'gets nowhere near', 'neraly decapties self instead of',
             'hit self on the foot, to the amusement of')
damage_report = ('small insult', 'flash wound','deep slash', 'ragged gash'
                 'savage laceration','fractured rib-cage',
                 'smashed-up face','split skull')
life_changing = ('a scar.','bruising','serious blood loss.',
                'total debilitation.','chronic concession.','a served limb.',
                'multiple fractures.','an amputated head.')