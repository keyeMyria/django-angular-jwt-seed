import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {ProgressBarService} from './progress-bar.service';
import {Error404Component} from '../errors/404.component';
import {Error500Component} from '../errors/500.component';
import {AuthenticationModule} from '../authentication';
import {BaseService} from '../shared/_services/base.service';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {ProfileRestDataSource} from '../dashboard/profile/rest.datasource';
import {TimingInterceptor} from '../shared/interceptors/timing.interceptor';
import {ProgressInterceptor} from '../shared/interceptors/progress.interceptor';

@NgModule({
  imports: [
    BrowserModule,
    AuthenticationModule, // AUTH MODULE
    HttpClientModule, // Include it under 'imports' in your application module after BrowserModule.
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule,

    //  SidemeuModule.forRoot()
  ],
  declarations: [
    Error404Component,
    Error500Component
  ],
  exports: [
    // TopbarModule, SidemenuModule, MainContentModule
  ],
})
export class CoreModule {
  static forRoot() {
    return {
      ngModule: CoreModule,
      providers: [
        BaseService,
        ProgressBarService,
        ProfileRestDataSource,
        {provide: HTTP_INTERCEPTORS, useClass: ProgressInterceptor, multi: true, deps: [ProgressBarService]},
        {provide: HTTP_INTERCEPTORS, useClass: TimingInterceptor, multi: true}
        // UserService, AuthService
      ]
    };
  }
}
