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
                        <label>Username:</label>
                        <input id="username" type="text" class="form-control" v-model="user.username"/>
                    </div>
                    <div class="form-group">
                        <label>Country:</label>
                        <input type="text" class="form-control" v-model="user.country"/>
                    </div>
                    <div class="form-group">
                        <label>Gender:</label>
                        <select class="form-control" v-model="user.gender">
                             <option v-for="option in options" v-bind:value="option.value">
                                {{ option.text }}
                            </option>
                        </select>
                    </div>
                    <div class="form-group">
                        <input type="submit" class="btn btn-primary" value="Update User"/>
                    </div>
                    <div v-if="error" class="alert alert-danger" role="alert">
                        <strong>Oh snap!</strong> Change a few things up and try submitting again.
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
                },
                options: [
                    { text: 'Male', value: 'M' },
                    { text: 'Female', value: 'F' },
                    { text: 'Other', value: 'O' }
                ],
                error:null
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
                    this.error = ""
                }).catch((_error) => {
                    this.error = _error;
                    console.error(this.error);
                });
            }
        }
    }
</script>