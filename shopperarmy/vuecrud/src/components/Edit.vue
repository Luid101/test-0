// Edit.vue

<template>
  <div class="container">
        <div class="card">
            <div class="card-header">
                <h3>Edit User</h3>
            </div>
            <div class="card-body">
                <form v-on:submit.prevent="updateUser">
                    <div class="form-group">
                        <label>username:</label>
                        <input id="username" type="text" class="form-control" v-model="user.username"/>
                    </div>
                    <div class="form-group">
                        <label>country:</label>
                        <input type="text" class="form-control" v-model="user.country"/>
                    </div>
                    <div class="form-group">
                        <label>gender(M/F/O):</label>
                        <input type="text" class="form-control" v-model="user.gender"/>
                    </div>
                    <div class="form-group">
                        <input type="submit" class="btn btn-primary" value="Update User"/>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
export default{
        data(){
            return{
                user:{},
                auth:{
                    username: process.env.VUE_APP_USER_NAME,
                    password: process.env.VUE_APP_PASSWORD
                }
            }
        },

        created: function(){
            this.getUser();
        },

        methods: {
            getUser()
            {
              let uri = 'http://localhost:8070/members/' + this.$route.params.id + '/?format=json';
                this.axios.get(uri).then((response) => {
                    this.user = response.data;
                });
            },

            updateUser()
            {
              let uri = 'http://localhost:8070/members/' + this.$route.params.id + "/";
              console.log(uri);
                this.axios.put(uri, this.user, {auth:this.auth}).then((response) => {
                    this.$router.push({name: 'Index'});
                });
            }
        }
    }
</script>