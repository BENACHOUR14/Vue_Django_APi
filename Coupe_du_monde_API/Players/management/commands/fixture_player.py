from django.core.management.base import BaseCommand, CommandError
from Players.models import Players

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.help = 'Insert players as fixtures'
        self.load_player()
        
    def load_player(self):
        Players.objects.all().delete()
        
        Players.objects.create(name='Kylian Mbappé', goals=8)
        Players.objects.create(name='Lionel Messi', goals=7)
        Players.objects.create(name='Julian Alvarez', goals=4)
        Players.objects.create(name='Olivier Giroud', goals=4)
        Players.objects.create(name='Alvaro Morata', goals=3)
        Players.objects.create(name='Bukayo Saka', goals=3)
        Players.objects.create(name='Cody Gakpo', goals=3)
        Players.objects.create(name='Gonçalo Ramos', goals=3)
        Players.objects.create(name='Marcus Rashford', goals=3)



