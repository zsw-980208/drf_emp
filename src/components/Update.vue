<template>
    <div id="wrap">
			<div id="top_content">
					<div id="header">
						<div id="rightheader">
							<p>
								2009/11/20
								<br />
							</p>
						</div>
						<div id="topheader">
							<h1 id="title">
								<a href="#">Main</a>
							</h1>
						</div>
						<div id="navigation">
						</div>
					</div>
				<div id="content">
					<p id="whereami">
					</p>
					<h1>
						update Emp info：{{$route.params.id}}
					</h1>
						<table cellpadding="0" cellspacing="0" border="0"
							class="form_table">
							<tr>
								<td valign="middle" align="right">
									id:
								</td>
								<td valign="middle" align="left">
									{{emp_list.id}}
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									name:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="name" v-model="emp_list.emp_name"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									photo:
								</td>
								<td valign="middle" align="left">
									<input type="file" name="photo" ref="photo"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									salary:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="salary" v-model="emp_list.salary"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									age:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="age" v-model="emp_list.age"/>
								</td>
							</tr>
						</table>
						<p>
							<input type="submit" class="button" value="提交修改" @click="update_emp"/>
						</p>
				</div>
			</div>
			<div id="footer">
				<div id="footer_bg">
					ABC@126.com
				</div>
			</div>
		</div>
</template>

<script>
    export default {
        name: "Update",
        data(){
          return{
            emp_id:"",
            emp_list:[],
            emp_name:"",
            img:"",
            salary:"",
            age:"",
          }
        },
        methods:{
          get_emp_id(){
            let emp_id=this.$route.params.id;
            this.$axios({
              url:"http://127.0.0.1:8000/api/emp/"+`${emp_id}`,
              method:"get"
          }).then(res=>{
              console.log(res.data.results);
              this.emp_list=res.data.results;
            }).catch(error=>{
              this.$message.error("查询出错了");
            })
          },
          update_emp(){
             let emp_id=this.$route.params.id;
             let formData = new FormData();
              formData.append("emp_name", this.emp_list.emp_name);
              formData.append("img", this.$refs.photo.files[0]);
              formData.append("salary", this.emp_list.salary);
              formData.append("age", this.emp_list.age);
              console
             this.$axios({
                url:"http://127.0.0.1:8000/api/emp/"+`${emp_id}`,
                method:"patch",
                data: formData,
                headers:{
                    'content-type': 'multipart/form-data'
                },
              }).then(res=>{
                console.log(res.data.results);
                 this.$router.push("/home")
                // this.emp_list=res.data.results;
              }).catch(error=>{
                this.$message.error("修改出错了");
              })
            }
        },
        created() {
            this.get_emp_id();
        }
    }
</script>

<style scoped>

</style>
