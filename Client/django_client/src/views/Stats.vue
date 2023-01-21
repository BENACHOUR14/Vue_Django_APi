<template>
    <div class="box">
        <h4 class="title">Les meilleurs buteurs de la coupe du monde : </h4>
        <div class="space"></div>
        <div class="grid">
            <div :key="player" v-for="player in JsonObj" class="card_player">
                <div class="stats">
                    <h5> {{player.name}} </h5>  <h5 class="goals"> {{"" + player.goals }} </h5>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default{
 

    async created() {
        await this.load_data();
    },
    data:function(){
        return{
            JsonObj :[]  
        }
    },
    methods:{
        load_data:async function()
        {
            axios.get(`http://localhost:8000/Players/`)
                .then(response => {
                // JSON responses are automatically parsed.
                this.JsonObj = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
        },
    },

}




</script>

  
  
<style scoped>
.box{
    max-width: 1500px;
    padding: 50px;
}

.space{
  height : 30px;
}

.spacing{
    width:400px;
}

.card_player
{
    border-radius: 15px;
    width: 800px;
    min-width: 200px;
    margin: 10px;
    background-color : var(--primary-light);
    box-shadow : var(--box-shadow);
    margin-left: 300px;
}

.stats
{
    padding: 20px;
    display: flex;
    flex-direction: row;
}

.goals
{
    position: absolute;
    right: 400px;
}

.grid{
  display:flex;
  flex-direction:row;
  flex-wrap: wrap;
  max-width: 1500px;
}
</style>
