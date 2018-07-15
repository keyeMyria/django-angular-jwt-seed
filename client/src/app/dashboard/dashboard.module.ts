import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SharedModule} from '../shared/shared.module';
import {ProfileComponent} from './profile/profile.component';
import {DashboardRoutingModule} from './dashboard-routing.module';
import {DashboardComponent} from './dashboard.component';


@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    DashboardRoutingModule,
  ],
  declarations: [
    DashboardComponent,
    ProfileComponent
  ],
  providers: [],
  exports: [
    DashboardComponent
  ]
})
export class DashboardModule {
}
