import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {LoginComponent} from './login.component';
import {LoginLayoutComponent} from './login-layout.component';

const routes: Routes = [
  {
    path: '',
    component: LoginLayoutComponent,
    pathMatch: 'full',
    children: [
      {
        path: '',
        component: LoginComponent
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoginRoutingModule {
}
