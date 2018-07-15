import {Injectable} from '@angular/core';

import {BehaviorSubject} from 'rxjs';

@Injectable({providedIn: 'root'})
export class MessagesService {
  snack_notification$ = new BehaviorSubject<any>(null);

  constructor() {
  }

}

