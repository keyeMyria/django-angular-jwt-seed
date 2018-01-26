import {Component} from '@angular/core';
import {Router} from '@angular/router';
import {AuthenticationService} from '../authentication';

@Component({
  selector: 'app-top-bar',
  template: `
    <mat-toolbar color="primary">
      <span>Application Title</span>

      <!-- This fills the remaining space of the current row -->
      <span class="example-fill-remaining-space"></span>

      <span>Right Aligned Text</span>
    </mat-toolbar>
  `
})
export class TopbarComponent {

  constructor() {
  }
}
