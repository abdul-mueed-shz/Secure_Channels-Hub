import { ROUTE_CONSTANTS } from "@/common/constants/routes";

export const routes = [
  {
    path: "/",
    children: [
      {
        // UserProfile will be rendered inside User's <router-view>
        // when /user/:id/profile is matched
        path: ROUTE_CONSTANTS.AUTH.PATH,
        name: ROUTE_CONSTANTS.AUTH.PATH,
        component: () => import("../views/AuthView.vue"),
      },
      {
        path: ROUTE_CONSTANTS.HOME.PATH,
        name: ROUTE_CONSTANTS.HOME.NAME,
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import("../views/HomeView.vue"),
      },
    ],
  },
];
