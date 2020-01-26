<template>
    <div class="card">
        <div class="card-header">
            <h3>Users</h3>
        </div>
        <table class="table table-hover">
            <thead>
            <tr>
                <td>Username</td>
                <td>Country</td>
                <td>Gender</td>
            </tr>
            </thead>

            <tbody>
                <tr v-for="_id in user_ids" :key="_id">
                    <td>{{ Users[_id].username }}</td>
                    <td>{{ Users[_id].country }}</td>
                    <td>{{ Users[_id].gender }}</td>
                    <td><router-link :to="{name: 'Edit', params: { id: _id }}" class="btn btn-primary">Edit</router-link></td>
                    <td><button class="btn btn-danger" v-on:click="deleteItem(_id)" >Delete</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

    export default {
        data(){
            return{
                Users: {},
                user_ids : [],
                auth:{
                    username: process.env.VUE_APP_USER_NAME,
                    password: process.env.VUE_APP_PASSWORD
                }
            }
        },

        created: function()
        {
            this.fetchUsers();
        },

        methods: {
            fetchUsers()
            {
              let uri = 'http://localhost:8070/members/?format=json';
              this.axios.get(uri).then((response) => {
                  response.data.forEach( user => {
                      this.Users[user.id] = user
                  });
                  this.user_ids = Object.keys(this.Users);
              });
            },

            deleteItem(id)
            {
                console.log(this.auth)
              let uri = 'http://localhost:8070/members/'+id+ "/";
              delete this.Users[id];
              this.user_ids = Object.keys(this.Users);
              this.axios.delete(uri, { auth: this.auth });
            }
        }
    }
</script>