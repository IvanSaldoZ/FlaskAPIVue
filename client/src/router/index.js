import Vue from 'vue';
import Router from 'vue-router';
// eslint-disable-next-line
import HelloWorld from '@/components/HelloWorld';
import Instagram from '@/components/Instagram';
import Books from '@/components/Books';
import Ping from '@/components/Ping';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Instagram',
      component: Instagram,
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'history',
});
