import { NgModule } from '@angular/core';
import { AUTH_SERVICE, AuthModule, PROTECTED_FALLBACK_PAGE_URI, PUBLIC_FALLBACK_PAGE_URI } from 'ngx-auth';

import { TokenStorage } from './services/token-storage.service';
import { AuthenticationService } from './services/authentication.service';
import { SharedModule } from '../shared/shared.module';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';

export function factory(authenticationService: AuthenticationService) {
  return authenticationService;
}

@NgModule({
  imports: [
    CommonModule,
    AuthModule,
    SharedModule
  ],
  declarations: [
    LoginComponent
  ],
  providers: [
    TokenStorage,
    AuthenticationService,
    { provide: PROTECTED_FALLBACK_PAGE_URI, useValue: '/' },
    { provide: PUBLIC_FALLBACK_PAGE_URI, useValue: '/login' },
    { provide: AUTH_SERVICE, deps: [AuthenticationService], useFactory: factory }
  ]
})
export class AuthenticationModule {

}
