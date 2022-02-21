import { createWebHistory, createRouter } from "vue-router";
const routes =  [
  {
    path: "/",
    alias: "/search",
    name: "search",
    component: () => import("./components/Search")
  },
  {
    path: "/krmaps",
    name: "krmaps",
    component: () => import("./components/KRMapsList")
  },
  {
    path: "/krmaps/:id",
    name: "krmap-details",
    component: () => import("./components/KRMap")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddKRMap")
  },
  {
    path: "/oauth2",
    name: "oauth2",
    component: () => import("./components/Oauth2")
  },
  {
    path: "/connlist",
    name: "connlist",
    component: () => import("./components/ConnectionList")
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;