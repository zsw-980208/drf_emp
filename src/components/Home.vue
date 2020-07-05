<template>
    <div id="wrap">
			<div id="top_content">
				<div id="header">
					<div id="rightheader">
						<p>
							2009/11/20
							<br />
              <a href="javascript:;" @click="quit">安全退出</a>
						</p>
					</div>
					<div id="topheader">
						<h1 id="title"><a href="#">main</a></h1>
					</div>
					<div id="navigation">
					</div>
				</div>
				<div id="content">
					<p id="whereami">
					</p>
					<h1>
						欢迎{{user_msg}}来到员工管理系统
					</h1>
					<table class="table">
						<tr class="table_header">
							<td>ID</td>
							<td>Name</td>
							<td>Photo</td>
							<td>Salary</td>
							<td>Age</td>
							<td>Operation</td>
						</tr>
						<tr v-for="emp in emp_list" :key="emp.id" :class="emp.id%2==0?'row2':'row1'">
							<td>{{emp.id}}</td>
							<td>{{emp.emp_name}}</td>
							<td><img :src="emp.img" style="height: 60px;"></td>
							<td>{{emp.salary}}</td>
              <td>{{emp.cate_age}}</td>
							<td>
<!--                <a href="javascript:;" @click="update_emp">修改员工</a>&nbsp;-->
                <router-link :to="'/update/'+emp.id">修改员工</router-link>
                <a href="javascript:;" @click="delemp(emp.id)">删除员工</a></td>
						</tr>
					</table>
					<p>
<!--						<input type="button" class="button" value="Add Employee"/>-->
              <el-button type="success"><router-link to="/addemp">添加员工</router-link></el-button>
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
        name: "Home",
        data(){
          return{
            user_msg : "",
            emp_list:[],
          }
        },


        methods:{
          allemp(){
            this.$axios({
              url: "http://127.0.0.1:8000/api/emp/",
              method: "get",
            }).then(res=>{
              console.log(res.data.results);
              this.emp_list=res.data.results;
            }).catch(error=>{
               this.$message.error("查询出错了");
            })
          },
          delemp(emp_id){
            console.log(emp_id);
            this.$axios({
              url: "http://127.0.0.1:8000/api/emp/"+`${emp_id}`,
              method: "delete",
            }).then(res=>{
              console.log(res.data.results);
              location.reload()
            }).catch(error=>{
               this.$message.error("删除出错了");
            })
          },
          quit(){
            sessionStorage.clear();
            this.$router.push("/login")
          }
        },
        created() {
          let username=sessionStorage.getItem("user");
          this.user_msg=username;
          if (username){

          } else{
            this.$message.error("请登录才能访问主页");
            this.$router.push("/login")
          }
          this.allemp()

        }
    }
</script>

<style scoped>

</style>
