import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";
import ProjectDetails from "../views/ProjectDetails.vue";

const routes = [
  { path: "/", component: Login },
  { path: "/register", component: Register },
  { path: "/dashboard", component: Dashboard, meta: { requiresAuth: true } },
  { path: "/projects/:id", component: ProjectDetails, name: "ProjectDetails", meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  const token = localStorage.getItem("token");
  if (to.meta.requiresAuth && !token) {
    return { path: "/" };
  }
  if ((to.path === "/" || to.path === "/register") && token) {
    return { path: "/dashboard" };
  }
  return true;
});

export default router;
