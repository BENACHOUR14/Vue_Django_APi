from django.core.management.base import BaseCommand, CommandError
from Teams.models import Teams

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.help = 'Insert teams as fixtures'
        self.load_teams()

    def load_teams(self):
        Teams.objects.all().delete()
        
        #Group_A
        Teams.objects.create(name='Pays-Bas', group='A', points=7, is_eliminated=False)
        Teams.objects.create(name='Sénégal', group='A', points=6, is_eliminated=False)
        Teams.objects.create(name='Equateur', group='A', points=4, is_eliminated=False)
        Teams.objects.create(name='Qatar', group='A', points=0, is_eliminated=False)

        #Group_B        
        Teams.objects.create(name='Angleterre', group='B', points=7, is_eliminated=False)
        Teams.objects.create(name='Etas-Unis', group='B', points=5, is_eliminated=False)
        Teams.objects.create(name='Iran', group='B', points=3, is_eliminated=False)
        Teams.objects.create(name='Pays de Galles', points=1, group='B', is_eliminated=False)

        #Group_C        
        Teams.objects.create(name='Argentine', group='C', points=6, is_eliminated=False)
        Teams.objects.create(name='Pologne', group='C', points=4, is_eliminated=False)
        Teams.objects.create(name='Mexique', group='C', points=4, is_eliminated=False)
        Teams.objects.create(name='Arabie saoudite', points=3, group='C', is_eliminated=False)

        #Group_D       
        Teams.objects.create(name='France', group='D', points=6, is_eliminated=False)
        Teams.objects.create(name='Australie', group='D', points=6, is_eliminated=False)
        Teams.objects.create(name='Tunisie', group='D', points=4, is_eliminated=False)
        Teams.objects.create(name='Danemark', group='D', points=1, is_eliminated=False)
        
        #Group_E       
        Teams.objects.create(name='Japon', group='E', points=6, is_eliminated=False)
        Teams.objects.create(name='Espagne', group='E', points=4, is_eliminated=False)
        Teams.objects.create(name='Allemagne', group='E', points=4, is_eliminated=False)
        Teams.objects.create(name='Costa Rica', group='E', points=3, is_eliminated=False)
        
        #Group_F       
        Teams.objects.create(name='Maroc', group='F', points=7, is_eliminated=False)
        Teams.objects.create(name='Croatie', group='F', points=5, is_eliminated=False)
        Teams.objects.create(name='Belgique', group='F', points=4, is_eliminated=False)
        Teams.objects.create(name='Canada', group='F', points=0, is_eliminated=False)
        
        #Group_G       
        Teams.objects.create(name='Brésil', group='G', points=6, is_eliminated=False)
        Teams.objects.create(name='Suisse', group='G', points=6, is_eliminated=False)
        Teams.objects.create(name='Cameroun', group='G', points=4, is_eliminated=False)
        Teams.objects.create(name='Serbie', group='G', points=1, is_eliminated=False)
        
        #Group_H       
        Teams.objects.create(name='Portugal', group='H', points=6, is_eliminated=False)
        Teams.objects.create(name='Corée du sud', group='H', points=4, is_eliminated=False)
        Teams.objects.create(name='Uruguay', group='H', points=4, is_eliminated=False)
        Teams.objects.create(name='Ghana', group='H', points=3, is_eliminated=False)

