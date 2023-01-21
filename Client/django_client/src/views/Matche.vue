<template>
    <div class="box">
        <h4 class="title">Resultat des matches de la coupe 2022 : </h4>
        <div class="space"></div>
        <div class="grid">
            <div :key="match" v-for="match in JsonObj" class="card">
                <div class="result">
                    <h5> {{match.home_team.name}} : {{match.goal_home_team}} </h5>
                    <h5> {{match.away_team.name}} : {{ match.goal_away_team}} </h5>
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
            JsonObj :[],
        }
    },
    methods:{
        load_data:async function()
        {
            axios.get(`http://127.0.0.1:8000/Games/`)
                .then(response => {
                // JSON responses are automatically parsed.
                this.JsonObj = response.data
                })
                .catch(e => {
                    console.log(e)
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

.card
{
    border-radius: 15px;
    width: 200px;
    min-width: 200px;
    margin: 10px;
    background-color : var(--primary-light);
    box-shadow : var(--box-shadow);
}

.result
{
    padding: 20px;
}

.grid{
  display:flex;
  flex-direction:row;
  flex-wrap: wrap;
  max-width: 1500px;
}
</style>
  