import {NgModule} from '@angular/core';
import {SharedModule} from '../shared/shared.module';
import {TopbarComponent} from './topbar.component';

@NgModule({
  imports: [
    SharedModule,
  ],
  declarations: [
    TopbarComponent
  ],
  exports: [
    TopbarComponent
  ]
})
export class TopbarModule {
}

@NgModule({
  imports: [],
  declarations: [
    // SidemenuComponent
  ],
  exports: [
    // SidemenuComponent
  ]
})
export class SidemenuModule {
  static forRoot() {   // pattern for adding app-wide services
    return {
      ngModule: SidemenuModule,
      providers: [
        // MenuSelectionService
      ]
    };
  }
}

@NgModule({
  imports: [
    // HomeModule, OtherModule,
  ],
  declarations: [
    // MainContentComponent
  ],
  exports: [
    // MainContentComponent
  ]
})
export class MainContentModule {
}

@NgModule({
  imports: [
    TopbarModule,
    SidemenuModule,
    MainContentModule,
  ],
  exports: [
    TopbarModule,
    SidemenuModule,
    MainContentModule,
  ],
})
export class LayoutModule {
}
