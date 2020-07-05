import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Home from "../components/Home";
import Addemp from "../components/Addemp";
import Update from "../components/Update";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path:'/',
      component:Login,
    },
    {
      path:'/login',
      component:Login,
    },
    {
      path:'/register',
      component:Register,
    },
    {
      path:'/home',
      component:Home,
    },
    {
      path:'/addemp',
      component:Addemp,
    },
    {
      path:'/update',
      component:Update,
    },
    {
      path:'/update/:id',
      component:Update,
    },
  ]
})
