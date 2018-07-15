import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {SharedModule} from './shared/shared.module';
import {CoreModule} from './core/core.module';
import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {BottomComponent, HeaderComponent, SidenavComponent} from './core/layout';


@NgModule({
  imports: [
    BrowserModule,
    CoreModule.forRoot(),  // forRoot so we get all the providers
    SharedModule,
    AppRoutingModule,
    BrowserAnimationsModule
  ],
  declarations: [
    AppComponent,
    HeaderComponent,
    SidenavComponent,
    BottomComponent,
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule {
}
