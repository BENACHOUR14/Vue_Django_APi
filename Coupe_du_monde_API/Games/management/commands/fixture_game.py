from django.core.management.base import BaseCommand
from Games.models import Games
from Teams.models import Teams
import datetime

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.help = 'Insert two games as fixtures'
        self.load_Games()
                   
    def load_Games(self):
        try:
            Games.objects.all().delete()
            
            #Group_A
            pays_bas = Teams.objects.get(name='Pays-Bas')
            senegal = Teams.objects.get(name='Sénégal')
            equateur = Teams.objects.get(name='Equateur')
            qatar = Teams.objects.get(name='Qatar')

            #Group_B        
            angleterre = Teams.objects.get(name='Angleterre')
            etas_unis = Teams.objects.get(name='Etas-Unis')
            iran = Teams.objects.get(name='Iran')
            pays_de_galles = Teams.objects.get(name='Pays de Galles')

            #Group_C        
            argentine = Teams.objects.get(name='Argentine')
            pologne = Teams.objects.get(name='Pologne')
            mexique = Teams.objects.get(name='Mexique')
            arabie_saoudite = Teams.objects.get(name='Arabie saoudite')

            #Group_D       
            france = Teams.objects.get(name='France')
            australie = Teams.objects.get(name='Australie')
            tunisie = Teams.objects.get(name='Tunisie')
            danemark = Teams.objects.get(name='Danemark')
        
            #Group_E       
            japon = Teams.objects.get(name='Japon')
            espagne = Teams.objects.get(name='Espagne')
            allemagne = Teams.objects.get(name='Allemagne')
            costa_rica = Teams.objects.get(name='Costa Rica')
        
            #Group_F       
            maroc = Teams.objects.get(name='Maroc')
            croatie = Teams.objects.get(name='Croatie')
            belgique = Teams.objects.get(name='Belgique')
            canada = Teams.objects.get(name='Canada')
        
            #Group_G       
            bresil = Teams.objects.get(name='Brésil')
            suisse = Teams.objects.get(name='Suisse')
            cameron = Teams.objects.get(name='Cameroun')
            serbie = Teams.objects.get(name='Serbie')
        
            #Group_H       
            portugal = Teams.objects.get(name='Portugal')
            coree_du_sud = Teams.objects.get(name='Corée du sud')
            uruguay = Teams.objects.get(name='Uruguay')
            ghana = Teams.objects.get(name='Ghana')
            
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=etas_unis, away_team=pays_de_galles, goal_home_team=1 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=belgique, away_team=canada, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=pays_de_galles, away_team=iran, goal_home_team=0 , goal_away_team=2 )
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=japon, away_team=costa_rica, goal_home_team=0 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=pays_de_galles, away_team=angleterre, goal_home_team=0 , goal_away_team=3)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=croatie, away_team=belgique, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.ahmed_bin_ali_stadium, home_team=argentine, away_team=australie, goal_home_team=2 , goal_away_team=1)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=danemark, away_team=tunisie, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=uruguay, away_team=coree_du_sud, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=pologne, away_team=arabie_saoudite, goal_home_team=2 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=coree_du_sud, away_team=ghana, goal_home_team=2 , goal_away_team=3)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=tunisie, away_team=france, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=coree_du_sud, away_team=portugal, goal_home_team=2 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=maroc, away_team=espagne, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.education_city_stadium, home_team=croatie, away_team=bresil, goal_home_team=1 , goal_away_team=1)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=france, away_team=australie, goal_home_team=4 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=suisse, away_team=cameron, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=tunisie, away_team=australie, goal_home_team=0 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=cameron, away_team=serbie, goal_home_team=3 , goal_away_team=3)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=australie, away_team=danemark, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=ghana, away_team=uruguay, goal_home_team=0 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_janoub_stadium, home_team=japon, away_team=croatie, goal_home_team=1 , goal_away_team=1)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=qatar, away_team=equateur, goal_home_team=0 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=maroc, away_team=croatie, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=angleterre, away_team=etas_unis, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=espagne, away_team=allemagne, goal_home_team=1 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=pays_bas, away_team=qatar, goal_home_team=2 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=costa_rica, away_team=allemagne, goal_home_team=2 , goal_away_team=4)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=angleterre, away_team=senegal, goal_home_team=3 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=angleterre, away_team=france, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_bayt_stadium, home_team=france, away_team=maroc, goal_home_team=2 , goal_away_team=0)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=senegal, away_team=pays_bas, goal_home_team=0 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=espagne, away_team=costa_rica, goal_home_team=7 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=qatar, away_team=senegal, goal_home_team=1 , goal_away_team=3)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=belgique, away_team=maroc, goal_home_team=0 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=iran, away_team=etas_unis, goal_home_team=0 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=canada, away_team=maroc, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=france, away_team=pologne, goal_home_team=3 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.al_thumama_stadium, home_team=maroc, away_team=portugal, goal_home_team=1 , goal_away_team=0)
            
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=mexique, away_team=pologne, goal_home_team=0 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=portugal, away_team=ghana, goal_home_team=3 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=france, away_team=danemark, goal_home_team=2 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=bresil, away_team=suisse, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=pologne, away_team=argentine, goal_home_team=0 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=serbie, away_team=suisse, goal_home_team=2 , goal_away_team=3)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.stadium_974, home_team=bresil, away_team=coree_du_sud, goal_home_team=4 , goal_away_team=1)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=angleterre, away_team=iran, goal_home_team=6 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=allemagne, away_team=japon, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=pays_bas, away_team=equateur, goal_home_team=1 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=croatie, away_team=canada, goal_home_team=4 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=equateur, away_team=senegal, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=japon, away_team=espagne, goal_home_team=2 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=pays_bas, away_team=etas_unis, goal_home_team=3 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.khalifa_international_stadium, home_team=croatie, away_team=maroc, goal_home_team=2 , goal_away_team=1)
            
            Games.objects.create(date=datetime.datetime.now(), stadium=Games.Stadium.lusail_stadium, home_team=argentine, away_team=arabie_saoudite, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=bresil, away_team=serbie, goal_home_team=2 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=argentine, away_team=mexique, goal_home_team=2 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=portugal, away_team=uruguay, goal_home_team=2 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=arabie_saoudite, away_team=mexique, goal_home_team=1 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=cameron, away_team=bresil, goal_home_team=1 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=portugal, away_team=suisse, goal_home_team=6 , goal_away_team=1)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=pays_bas, away_team=argentine, goal_home_team=2 , goal_away_team=2)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=argentine, away_team=croatie, goal_home_team=3 , goal_away_team=0)
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=argentine, away_team=france, goal_home_team=3 , goal_away_team=3)


        except Teams.DoesNotExist:
            print("Please Add Teams First")
