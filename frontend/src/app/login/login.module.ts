import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';

import {LoginRoutingModule} from './login-routing.module';
import {LoginComponent} from './login.component';
import {SharedModule} from '../shared/shared.module';
import {LoginLayoutComponent} from './login-layout.component';

@NgModule({
  imports: [
    CommonModule,
    LoginRoutingModule,
    SharedModule,
  ],
  declarations: [
    LoginComponent,
    LoginLayoutComponent
  ]
})
export class LoginModule {
}
