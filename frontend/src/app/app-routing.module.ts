import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {Error404Component} from './errors/404.component';
import {Error500Component} from './errors/500.component';

import {PublicGuard, ProtectedGuard} from 'ngx-auth';

const AppRoutes: Routes = [
  {
    path: 'login',
    canActivate: [
      PublicGuard
    ],
    loadChildren: './login/login.module#LoginModule'
  },
  {
    path: '404', component: Error404Component
  },
  {
    path: '500', component: Error500Component
  },
  {
    path: '',
    canActivate: [
      ProtectedGuard
    ],
    loadChildren: './dashboard/dashboard.module#DashboardModule'
  },
  {path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [
    RouterModule.forRoot(AppRoutes)
  ],
  exports: [
    RouterModule
  ]
})

export class AppRoutingModule {
}
