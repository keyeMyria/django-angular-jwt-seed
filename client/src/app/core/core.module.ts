import {NgModule} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {BrowserModule} from '@angular/platform-browser';
import {AuthenticationModule} from '../authentication';
import {Error404Component, Error500Component} from '../errors/';
import {ProgressInterceptor, TimingInterceptor} from '../shared/interceptors/';
import {ProgressBarService} from '../shared/services/';
import {ProfileSourceService} from '../dashboard';

@NgModule({
  imports: [
    BrowserModule,
    AuthenticationModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule
  ],
  declarations: [
    Error404Component,
    Error500Component
  ],
  exports: []
})
export class CoreModule {
  static forRoot() {
    return {
      ngModule: CoreModule,
      providers: [
        ProfileSourceService,
        ProgressBarService,
        {provide: HTTP_INTERCEPTORS, useClass: ProgressInterceptor, multi: true, deps: [ProgressBarService]},
        {provide: HTTP_INTERCEPTORS, useClass: TimingInterceptor, multi: true}
      ]
    };
  }
}
