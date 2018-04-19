import {ModuleWithProviders, NgModule} from '@angular/core';
import {MaterialModule} from './modules/material.module';
import {FlexLayoutModule} from '@angular/flex-layout';
import {ReactiveFormsModule} from '@angular/forms';
import {ClarityModule} from '@clr/angular';

import '@clr/icons';
import '@clr/icons/shapes/essential-shapes';
import '@clr/icons/shapes/technology-shapes';

@NgModule({
  imports: [
    ReactiveFormsModule,
    MaterialModule,
    FlexLayoutModule,
    ClarityModule,
  ],
  providers: [],
  exports: [
    ReactiveFormsModule,
    MaterialModule,
    FlexLayoutModule,
    ClarityModule
  ]
})
export class SharedModule {
  static forRoot(): ModuleWithProviders {
    return {
      ngModule: SharedModule,
      providers: []
    };
  }
}
