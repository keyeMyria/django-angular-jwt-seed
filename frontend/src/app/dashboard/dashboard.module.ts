import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';

import {DashboardRoutingModule} from './dashboard-routing.module';
import {DashboardComponent} from './main/dashboard.component';
import {DashboardLayoutComponent} from './dashboard-layout.component';
import {LayoutModule} from '../layout/layout.module';
import {ProfileComponent} from './profile/profile.component';

@NgModule({
  imports: [
    CommonModule,
    DashboardRoutingModule,
    LayoutModule,
  ],
  declarations: [
    DashboardComponent,
    DashboardLayoutComponent,
    ProfileComponent
  ],
  providers: [],
})
export class DashboardModule {
}
