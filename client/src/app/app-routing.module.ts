import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {Error404Component, Error500Component} from './errors/';

import {ProtectedGuard, PublicGuard} from 'ngx-auth';
import {LoginComponent} from './authentication/';

const AppRoutes: Routes = [
  {path: '', redirectTo: '/dashboard', pathMatch: 'full'},
  {path: 'login', canActivate: [PublicGuard], component: LoginComponent},
  {path: 'dashboard', canActivate: [ProtectedGuard], loadChildren: './dashboard/dashboard.module#DashboardModule'},
  {path: '404', component: Error404Component},
  {path: '500', component: Error500Component},
  {path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      AppRoutes
      // { enableTracing: true }
    )
  ],
  exports: [
    RouterModule
  ]
})

export class AppRoutingModule {
}
