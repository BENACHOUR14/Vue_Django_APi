<template>
    <div class="box">
        <h4 class="title">Resultat de matche de la coupe 2022 : </h4>
        <div class="space"></div>
        <div class="grid">

            <div class="card">
                <h4 class="groupe_name">Groupe A</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeA">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe B</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeB">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe C</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeC">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe D</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeD">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe E</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeE">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe F</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeF">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe G</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeG">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
            </div>

            <div class="card">
                <h4 class="groupe_name">Groupe H</h4>
                    <table>
                        <tr>
                            <th> team </th>
                            <th> points </th>
                        </tr>
                        <tr :key="team" v-for="team in GroupeH">
                            <td> {{team.name}} </td>
                            <td> {{team.points}} </td>
                        </tr>
                    </table>
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
    data:function()
    {
       return {
        GroupeA:[],
        GroupeB:[],
        GroupeC:[],
        GroupeD:[],
        GroupeE:[],
        GroupeF:[],
        GroupeG:[],
        GroupeH:[]
    }},
    methods:{
        load_data:function()
        {
            axios.get(`http://localhost:8000/Teams/?group=A`)
                .then(response => {
                // JSON responses are automatically parsed.
                this.GroupeA = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })

            axios.get(`http://localhost:8000/Teams/?group=B`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeB = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=C`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeC = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=D`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeD = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=E`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeE = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=F`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeF = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=G`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeG = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            axios.get(`http://localhost:8000/Teams/?group=H`)
            .then(response => {
            // JSON responses are automatically parsed.
            this.GroupeH = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
        }
    },

}

</script>

  
  
<style scoped>

.groupe_name
{
    padding: 5px;
    justify-content: center;
    text-align: center;
}
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
    width: 400px;
    min-width: 200px;
    margin: 10px;
    background-color : var(--primary-light);
    box-shadow : var(--box-shadow);
}

table
{
    padding: 10px;
    justify-content: center;
    text-align: center;
    width: 400px;
}

table td{
    border: 1px solid;
}

table th{
    border: 1px solid;
}

.grid{
  display:flex;
  flex-direction:row;
  flex-wrap: wrap;
  max-width: 1500px;
}
</style>
  